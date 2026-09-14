; ModuleID = 'algorithms/02_c/dp/lis.c'
source_filename = "algorithms/02_c/dp/lis.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@__const.main.a = private unnamed_addr constant [8 x i32] [i32 10, i32 9, i32 2, i32 5, i32 3, i32 7, i32 101, i32 18], align 16
@.str = private unnamed_addr constant [35 x i8] c"[C LIS] FAILED: length %d, want 4\0A\00", align 1
@str = private unnamed_addr constant [61 x i8] c"[C LIS] Longest increasing subsequence verified (O(n log n))\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: read) uwtable
define dso_local i32 @lis_length(ptr noundef readonly captures(none) %0, i32 noundef %1) local_unnamed_addr #0 {
  %3 = alloca [100000 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %3) #5
  %4 = icmp sgt i32 %1, 0
  br i1 %4, label %5, label %13

5:                                                ; preds = %2
  %6 = zext nneg i32 %1 to i64
  br label %7

7:                                                ; preds = %5, %28
  %8 = phi i64 [ 0, %5 ], [ %35, %28 ]
  %9 = phi i32 [ 0, %5 ], [ %34, %28 ]
  %10 = icmp eq i32 %9, 0
  %11 = getelementptr inbounds nuw i32, ptr %0, i64 %8
  %12 = load i32, ptr %11, align 4, !tbaa !5
  br i1 %10, label %28, label %15

13:                                               ; preds = %28, %2
  %14 = phi i32 [ 0, %2 ], [ %34, %28 ]
  call void @llvm.lifetime.end.p0(ptr nonnull %3) #5
  ret i32 %14

15:                                               ; preds = %7, %15
  %16 = phi i32 [ %26, %15 ], [ %9, %7 ]
  %17 = phi i32 [ %25, %15 ], [ 0, %7 ]
  %18 = add nsw i32 %16, %17
  %19 = sdiv i32 %18, 2
  %20 = sext i32 %19 to i64
  %21 = getelementptr inbounds i32, ptr %3, i64 %20
  %22 = load i32, ptr %21, align 4, !tbaa !5
  %23 = icmp slt i32 %22, %12
  %24 = add nsw i32 %19, 1
  %25 = select i1 %23, i32 %24, i32 %17
  %26 = select i1 %23, i32 %16, i32 %19
  %27 = icmp slt i32 %25, %26
  br i1 %27, label %15, label %28, !llvm.loop !9

28:                                               ; preds = %15, %7
  %29 = phi i32 [ 0, %7 ], [ %25, %15 ]
  %30 = sext i32 %29 to i64
  %31 = getelementptr inbounds i32, ptr %3, i64 %30
  store i32 %12, ptr %31, align 4, !tbaa !5
  %32 = icmp eq i32 %29, %9
  %33 = zext i1 %32 to i32
  %34 = add nuw nsw i32 %9, %33
  %35 = add nuw nsw i64 %8, 1
  %36 = icmp eq i64 %35, %6
  br i1 %36, label %13, label %7, !llvm.loop !11
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  %1 = alloca [100000 x i32], align 16
  %2 = alloca [100000 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %2) #5
  br label %3

3:                                                ; preds = %22, %0
  %4 = phi i64 [ 0, %0 ], [ %29, %22 ]
  %5 = phi i32 [ 0, %0 ], [ %28, %22 ]
  %6 = icmp eq i32 %5, 0
  %7 = getelementptr inbounds nuw i32, ptr @__const.main.a, i64 %4
  %8 = load i32, ptr %7, align 4, !tbaa !5
  br i1 %6, label %22, label %9

9:                                                ; preds = %3, %9
  %10 = phi i32 [ %20, %9 ], [ %5, %3 ]
  %11 = phi i32 [ %19, %9 ], [ 0, %3 ]
  %12 = add nsw i32 %11, %10
  %13 = sdiv i32 %12, 2
  %14 = sext i32 %13 to i64
  %15 = getelementptr inbounds i32, ptr %2, i64 %14
  %16 = load i32, ptr %15, align 4, !tbaa !5
  %17 = icmp slt i32 %16, %8
  %18 = add nsw i32 %13, 1
  %19 = select i1 %17, i32 %18, i32 %11
  %20 = select i1 %17, i32 %10, i32 %13
  %21 = icmp slt i32 %19, %20
  br i1 %21, label %9, label %22, !llvm.loop !9

22:                                               ; preds = %9, %3
  %23 = phi i32 [ 0, %3 ], [ %19, %9 ]
  %24 = sext i32 %23 to i64
  %25 = getelementptr inbounds i32, ptr %2, i64 %24
  store i32 %8, ptr %25, align 4, !tbaa !5
  %26 = icmp eq i32 %23, %5
  %27 = zext i1 %26 to i32
  %28 = add nuw nsw i32 %5, %27
  %29 = add nuw nsw i64 %4, 1
  %30 = icmp eq i64 %29, 8
  br i1 %30, label %31, label %3, !llvm.loop !11

31:                                               ; preds = %22
  call void @llvm.lifetime.end.p0(ptr nonnull %2) #5
  %32 = icmp eq i32 %28, 4
  br i1 %32, label %64, label %33

33:                                               ; preds = %31
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #5
  br label %34

34:                                               ; preds = %53, %33
  %35 = phi i64 [ 0, %33 ], [ %60, %53 ]
  %36 = phi i32 [ 0, %33 ], [ %59, %53 ]
  %37 = icmp eq i32 %36, 0
  %38 = getelementptr inbounds nuw i32, ptr @__const.main.a, i64 %35
  %39 = load i32, ptr %38, align 4, !tbaa !5
  br i1 %37, label %53, label %40

40:                                               ; preds = %34, %40
  %41 = phi i32 [ %51, %40 ], [ %36, %34 ]
  %42 = phi i32 [ %50, %40 ], [ 0, %34 ]
  %43 = add nsw i32 %42, %41
  %44 = sdiv i32 %43, 2
  %45 = sext i32 %44 to i64
  %46 = getelementptr inbounds i32, ptr %1, i64 %45
  %47 = load i32, ptr %46, align 4, !tbaa !5
  %48 = icmp slt i32 %47, %39
  %49 = add nsw i32 %44, 1
  %50 = select i1 %48, i32 %49, i32 %42
  %51 = select i1 %48, i32 %41, i32 %44
  %52 = icmp slt i32 %50, %51
  br i1 %52, label %40, label %53, !llvm.loop !9

53:                                               ; preds = %40, %34
  %54 = phi i32 [ 0, %34 ], [ %50, %40 ]
  %55 = sext i32 %54 to i64
  %56 = getelementptr inbounds i32, ptr %1, i64 %55
  store i32 %39, ptr %56, align 4, !tbaa !5
  %57 = icmp eq i32 %54, %36
  %58 = zext i1 %57 to i32
  %59 = add nuw nsw i32 %36, %58
  %60 = add nuw nsw i64 %35, 1
  %61 = icmp eq i64 %60, 8
  br i1 %61, label %62, label %34, !llvm.loop !11

62:                                               ; preds = %53
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #5
  %63 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %59)
  br label %66

64:                                               ; preds = %31
  %65 = tail call i32 @puts(ptr nonnull dereferenceable(1) @str)
  br label %66

66:                                               ; preds = %64, %62
  %67 = phi i32 [ 1, %62 ], [ 0, %64 ]
  ret i32 %67
}

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #3

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #4

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: read) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { nofree nounwind }
attributes #5 = { nounwind }

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
!11 = distinct !{!11, !10}
