; ModuleID = 'algorithms/02_c/techniques/prefix_sum.c'
source_filename = "algorithms/02_c/techniques/prefix_sum.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@str = private unnamed_addr constant [48 x i8] c"[C PrefixSum] Prefix sum range queries verified\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local void @prefix_build(ptr noundef readonly captures(none) %0, i32 noundef %1, ptr noundef writeonly captures(none) initializes((0, 8)) %2) local_unnamed_addr #0 {
  store i64 0, ptr %2, align 8, !tbaa !9
  %4 = icmp sgt i32 %1, 0
  br i1 %4, label %5, label %29

5:                                                ; preds = %3
  %6 = zext nneg i32 %1 to i64
  %7 = and i64 %6, 3
  %8 = icmp ult i32 %1, 4
  br i1 %8, label %13, label %9

9:                                                ; preds = %5
  %10 = and i64 %6, 2147483644
  br label %30

11:                                               ; preds = %30
  %12 = icmp eq i64 %7, 0
  br i1 %12, label %29, label %13

13:                                               ; preds = %11, %5
  %14 = phi i64 [ 0, %5 ], [ %55, %11 ]
  %15 = phi i64 [ 0, %5 ], [ %56, %11 ]
  %16 = icmp ne i64 %7, 0
  tail call void @llvm.assume(i1 %16)
  br label %17

17:                                               ; preds = %17, %13
  %18 = phi i64 [ %14, %13 ], [ %24, %17 ]
  %19 = phi i64 [ %15, %13 ], [ %25, %17 ]
  %20 = phi i64 [ 0, %13 ], [ %27, %17 ]
  %21 = getelementptr inbounds nuw i32, ptr %0, i64 %19
  %22 = load i32, ptr %21, align 4, !tbaa !5
  %23 = sext i32 %22 to i64
  %24 = add nsw i64 %18, %23
  %25 = add nuw nsw i64 %19, 1
  %26 = getelementptr inbounds nuw i64, ptr %2, i64 %25
  store i64 %24, ptr %26, align 8, !tbaa !9
  %27 = add i64 %20, 1
  %28 = icmp eq i64 %27, %7
  br i1 %28, label %29, label %17, !llvm.loop !11

29:                                               ; preds = %11, %17, %3
  ret void

30:                                               ; preds = %30, %9
  %31 = phi i64 [ 0, %9 ], [ %55, %30 ]
  %32 = phi i64 [ 0, %9 ], [ %56, %30 ]
  %33 = phi i64 [ 0, %9 ], [ %58, %30 ]
  %34 = getelementptr inbounds nuw i32, ptr %0, i64 %32
  %35 = load i32, ptr %34, align 4, !tbaa !5
  %36 = sext i32 %35 to i64
  %37 = add nsw i64 %31, %36
  %38 = or disjoint i64 %32, 1
  %39 = getelementptr inbounds nuw i64, ptr %2, i64 %38
  store i64 %37, ptr %39, align 8, !tbaa !9
  %40 = getelementptr inbounds nuw i32, ptr %0, i64 %38
  %41 = load i32, ptr %40, align 4, !tbaa !5
  %42 = sext i32 %41 to i64
  %43 = add nsw i64 %37, %42
  %44 = or disjoint i64 %32, 2
  %45 = getelementptr inbounds nuw i64, ptr %2, i64 %44
  store i64 %43, ptr %45, align 8, !tbaa !9
  %46 = getelementptr inbounds nuw i32, ptr %0, i64 %44
  %47 = load i32, ptr %46, align 4, !tbaa !5
  %48 = sext i32 %47 to i64
  %49 = add nsw i64 %43, %48
  %50 = or disjoint i64 %32, 3
  %51 = getelementptr inbounds nuw i64, ptr %2, i64 %50
  store i64 %49, ptr %51, align 8, !tbaa !9
  %52 = getelementptr inbounds nuw i32, ptr %0, i64 %50
  %53 = load i32, ptr %52, align 4, !tbaa !5
  %54 = sext i32 %53 to i64
  %55 = add nsw i64 %49, %54
  %56 = add nuw nsw i64 %32, 4
  %57 = getelementptr inbounds nuw i64, ptr %2, i64 %56
  store i64 %55, ptr %57, align 8, !tbaa !9
  %58 = add i64 %33, 4
  %59 = icmp eq i64 %58, %10
  br i1 %59, label %11, label %30, !llvm.loop !13
}

; Function Attrs: mustprogress nofree norecurse nosync nounwind sspstrong willreturn memory(argmem: read) uwtable
define dso_local i64 @prefix_range(ptr noundef readonly captures(none) %0, i32 noundef %1, i32 noundef %2) local_unnamed_addr #1 {
  %4 = sext i32 %2 to i64
  %5 = getelementptr i64, ptr %0, i64 %4
  %6 = getelementptr i8, ptr %5, i64 8
  %7 = load i64, ptr %6, align 8, !tbaa !9
  %8 = sext i32 %1 to i64
  %9 = getelementptr inbounds i64, ptr %0, i64 %8
  %10 = load i64, ptr %9, align 8, !tbaa !9
  %11 = sub nsw i64 %7, %10
  ret i64 %11
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local noundef range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  %1 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str)
  ret i32 0
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #3

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write)
declare void @llvm.assume(i1 noundef) #4

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nofree norecurse nosync nounwind sspstrong willreturn memory(argmem: read) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind }
attributes #4 = { nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write) }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = !{!10, !10, i64 0}
!10 = !{!"long long", !7, i64 0}
!11 = distinct !{!11, !12}
!12 = !{!"llvm.loop.unroll.disable"}
!13 = distinct !{!13, !14}
!14 = !{!"llvm.loop.mustprogress"}
