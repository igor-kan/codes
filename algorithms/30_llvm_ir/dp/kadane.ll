; ModuleID = 'algorithms/02_c/dp/kadane.c'
source_filename = "algorithms/02_c/dp/kadane.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@str = private unnamed_addr constant [41 x i8] c"[C Kadane] Maximum subarray sum verified\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: read) uwtable
define dso_local i32 @kadane(ptr noundef readonly captures(none) %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = load i32, ptr %0, align 4, !tbaa !5
  %4 = icmp sgt i32 %1, 1
  br i1 %4, label %5, label %24

5:                                                ; preds = %2
  %6 = zext nneg i32 %1 to i64
  %7 = add nsw i64 %6, -1
  %8 = and i64 %7, 1
  %9 = icmp eq i32 %1, 2
  br i1 %9, label %14, label %10

10:                                               ; preds = %5
  %11 = and i64 %7, -2
  br label %26

12:                                               ; preds = %26
  %13 = icmp eq i64 %8, 0
  br i1 %13, label %24, label %14

14:                                               ; preds = %12, %5
  %15 = phi i64 [ 1, %5 ], [ %42, %12 ]
  %16 = phi i32 [ %3, %5 ], [ %40, %12 ]
  %17 = phi i32 [ %3, %5 ], [ %41, %12 ]
  %18 = icmp ne i64 %8, 0
  tail call void @llvm.assume(i1 %18)
  %19 = tail call i32 @llvm.smax.i32(i32 %16, i32 0)
  %20 = getelementptr inbounds nuw i32, ptr %0, i64 %15
  %21 = load i32, ptr %20, align 4, !tbaa !5
  %22 = add nsw i32 %21, %19
  %23 = tail call i32 @llvm.smax.i32(i32 %22, i32 %17)
  br label %24

24:                                               ; preds = %14, %12, %2
  %25 = phi i32 [ %3, %2 ], [ %41, %12 ], [ %23, %14 ]
  ret i32 %25

26:                                               ; preds = %26, %10
  %27 = phi i64 [ 1, %10 ], [ %42, %26 ]
  %28 = phi i32 [ %3, %10 ], [ %40, %26 ]
  %29 = phi i32 [ %3, %10 ], [ %41, %26 ]
  %30 = phi i64 [ 0, %10 ], [ %43, %26 ]
  %31 = tail call i32 @llvm.smax.i32(i32 %28, i32 0)
  %32 = getelementptr inbounds nuw i32, ptr %0, i64 %27
  %33 = load i32, ptr %32, align 4, !tbaa !5
  %34 = add nsw i32 %33, %31
  %35 = tail call i32 @llvm.smax.i32(i32 %34, i32 %29)
  %36 = tail call i32 @llvm.smax.i32(i32 %34, i32 0)
  %37 = getelementptr inbounds nuw i32, ptr %0, i64 %27
  %38 = getelementptr inbounds nuw i8, ptr %37, i64 4
  %39 = load i32, ptr %38, align 4, !tbaa !5
  %40 = add nsw i32 %39, %36
  %41 = tail call i32 @llvm.smax.i32(i32 %40, i32 %35)
  %42 = add nuw nsw i64 %27, 2
  %43 = add i64 %30, 2
  %44 = icmp eq i64 %43, %11
  br i1 %44, label %12, label %26, !llvm.loop !9
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local noundef range(i32 0, 2) i32 @main() local_unnamed_addr #1 {
  %1 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str)
  ret i32 0
}

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smax.i32(i32, i32) #2

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #3

; Function Attrs: nocallback nofree nosync nounwind willreturn memory(inaccessiblemem: write)
declare void @llvm.assume(i1 noundef) #4

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: read) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }
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
!9 = distinct !{!9, !10}
!10 = !{!"llvm.loop.mustprogress"}
